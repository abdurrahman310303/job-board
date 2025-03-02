# Job Board Application

## Overview
This is a **Django-based Job Board** application that allows users to:
- View job listings
- Filter jobs by **location, role, job type, and company**
- Click on a job to view **detailed information**

## Features
✅ List of jobs with essential details (title, company, location, salary)  
✅ Search and filter jobs by location, role, job type, and company  
✅ Job detail page with full job description  
✅ Responsive and user-friendly interface  

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/abdurrahman310303/job-board.git
   cd job-board
   ```

2. **Create a Virtual Environment** (Recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```sh
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```

6. **Access the Application**
   Open a browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

## Usage
1. Browse available jobs on the homepage.
2. Use the **filter options** to refine job searches.
3. Click on a job title to view detailed information.

## Project Structure
```
job-board/
├── jobs/               # Django app for job listings
│   ├── templates/jobs/ # HTML templates
│   ├── models.py       # Job model definition
│   ├── views.py        # Views handling job listing and details
│   ├── urls.py         # URL routing
├── job_board/          # Django project files
├── db.sqlite3          # Database file
├── manage.py           # Django project manager
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

## Contributing
Contributions are welcome! Feel free to fork the repo, make changes, and submit a pull request.

## Contact
📧 Email: [Your Email]  
🔗 LinkedIn: [Abdur Rahman](www.linkedin.com/in/abdur-rahman-5b6907239)  
🐙 GitHub: [abdurrahman310303](https://github.com/abdurrahman310303)  

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
🎯 **Happy Coding!** 🚀

