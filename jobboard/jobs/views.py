from django.shortcuts import render, get_object_or_404
from .models import Job

def job_list(request):
    jobs = Job.objects.all()

    # Get filter values from the request
    location = request.GET.get('location', '')
    role = request.GET.get('role', '')
    job_type = request.GET.get('job_type', '')
    company = request.GET.get('company', '')

    # Apply filters if values are provided
    if location:
        jobs = jobs.filter(location__icontains=location)
    if role:
        jobs = jobs.filter(title__icontains=role)
    if job_type:
        jobs = jobs.filter(job_type__icontains=job_type)
    if company:
        jobs = jobs.filter(company__icontains=company)

    # Get unique values for filter dropdowns
    locations = Job.objects.values_list('location', flat=True).distinct()
    roles = Job.objects.values_list('title', flat=True).distinct()
    job_types = Job.objects.values_list('job_type', flat=True).distinct()
    companies = Job.objects.values_list('company', flat=True).distinct()

    context = {
        'jobs': jobs,
        'locations': locations,
        'roles': roles,
        'job_types': job_types,
        'companies': companies,
    }

    return render(request, 'jobs/job_list.html', context)

def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})
