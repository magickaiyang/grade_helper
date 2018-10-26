# grade_helper for CS193

View consecutive web pages for grading with usernames pulled from a file, and record grades as you go.
It reduces the need for copying and pasting, switching tabs, and navigating google sheets.

## Setup
1. Clone
2. Examine ```base_url``` variable, tailor it to fit your need.
3. Fill ```token``` variable with your GitHub personal access token.
> * Get it from you GitHub account Settings page, as shown below
> ![g](/info/GitHub_token.PNG)
4. Edit github_usernames.txt to contain a list of students' GitHub username, separated by \n. You could copy the entire column from Lab Grading Sheet.
5. Run web_grade_helper.py
6. Copy the grades in grades.txt to google sheet. Copy all and paste to the entire column.

## Considerations
* Keep your GitHub token safe
* Make sure the grades.txt from previous runs is deleted
* Make sure github_usernames.txt is in the current working directory
* Python 3.x required. On Windows, click the ```web_grade_helper.py``` file to run. On macOS or Linux, use ```python3 web_grade_helper.py```
to run.
