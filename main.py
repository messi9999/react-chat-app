import subprocess
import random
import datetime
import time


def run_func():
    days = 217
    while days > 150:
        commit_array = ["updated", "commit", "updated main function", "updated import", "hello", "second", "readme update", "new variable", "new", "const updated", "main function", "content", "script", "old command", "replace", "read", "no", "add another function", "javascript", "functional component", "component", "ugent update", "responsive", "last update", "include bash script"]
        days_array = [0, 0, 0, 0, 1, 1, 2, 3]

        concenpt_array = [
            "Other non-technical skills like communication in 2 sentences",
            "Experience with technical details in 2 sentences",
            "Tech stacks which are good fit for this project",
            "Introduction of my career in 1 or 2 sentences",
            "I was elated to see an opening for this project.",
            "I can't wait to bring my experience in developing algorithms and devising high-performance machine learning systems to you",
            "I am the Machine Learning Engineer at computer vision Technology.",
            "As someone who has been passionate about machine learning for a long time, I would love to do you project.",
            "Thank you for your time and consideration. I am eager to discuss my qualifications further.",
            "After reviewing your job description, I was impressed with this project.",
            "I have recently completed my previous project, where I was assigned to the team of Machine Learning and Artificial Intelligence.",
            "I worked on the development of tools that were able to predict failures in the",
            "mainframe system and the development of various machine learning and natural ",
            "I also integrate lots of machine learning projects into web and mobile applications.",
            "I believe that skills and knowledge in this field will allow me to quickly adapt to your",
            "organization's needs. I would welcome the opportunity to interview for this project."

        ]
        # Specify the path to the shell script
        script_path = './run.sh'
        script_contents = ''
        # Read the contents of the shell script
        with open(script_path, 'r') as file:
            script_contents = file.read()
        
        with open("./concepts.txt", "w") as file:
            file.write(random.choice(concenpt_array))

        # Modify the script contents
        # For example, let's replace a specific line with a new command  
        
        commit = random.choice(commit_array)
        old_command = script_contents
        new_command = """
clear
git status
git add .
git commit --date="{} day ago" -m "{}"
git push origin main
        """.format(days, commit)

        updated_contents = script_contents.replace(old_command, new_command)

        # Write the updated contents back to the shell script
        with open(script_path, 'w') as file:
            file.write(updated_contents)
        time.sleep(1)

        # Run the updated shell script
        subprocess.run(['bash', script_path])
        time.sleep(random.choice([5, 6, 7, 8, 9, 10, 8, 6, 7]))
        days = days - random.choice(days_array)

if __name__ == "__main__":
    run_func()