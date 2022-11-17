import subprocess
import random
import datetime
import time


def run_func():
    days = 225
    while days > 150:
        commit_array = ["updated", "commit", "updated main function", "updated import", "hello", "second", "readme update", "new variable", "new", "const updated", "main function", "content", "script", "old command", "replace", "read", "no", "add another function", "javascript", "functional component", "component", "ugent update", "responsive", "last update", "include bash script"]
        days_array = [0, 0, 0, 0, 0, 1, 1, 2, 3]
        # Specify the path to the shell script
        script_path = './run.sh'
        script_contents = ''
        # Read the contents of the shell script
        with open(script_path, 'r') as file:
            script_contents = file.read()

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
        time.sleep(9)
        days = days - random.choice(days_array)

if __name__ == "__main__":
    run_func()