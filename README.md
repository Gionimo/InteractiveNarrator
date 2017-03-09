# Interactive Narrator
**Developed @ Utrecht University**

Visualize your user stories to improve understanding of the project, inspect system functionality 
and imporve communication among stakeholders.

This application uses the Visual Narrator (https://github.com/marcelrobeer/visualnarrator) to generate a conceptual model which is then
visualized using Vis.js and is presented to the user in the browser from where the visualization can be modified to cater to the 
user's needs.

![alt tag](https://raw.githubusercontent.com/Gionimo/InteractiveNarrator/master/ScreenshotInteractiveNarrator.png)
![alt tag](https://github.com/Gionimo/InteractiveNarrator/blob/master/Screenshot%20Interactive%20Narrator)
![Screenshot](Screenshot Interactive Narrator.png)

**Dependencies**
This program has been and tested to run with Python 3.5.2. It has been tested to work with Ubuntu 16.04 and the instructions below are based on Ubuntu being on your machine. 
The main dependency for the program is Visual Narrator (https://github.com/marcelrobeer/visualnarrator). 
To run the Interactive Narrator, you need to install Visual Narrator in the same directory as the Interactive Narrator folder is in (/InteractiveNarrator) Other depencies can be found in requirements.txt

**Installation**
Currently, Interactive Narrator needs to be run from your local machine. I assume you have Python3 installed system wide and have pip setup tools installed too. If not install pip (Linux) with: 'sudo apt-get install python-setuptools python-dev build-essential'. Then, the preferred method is to create a virtual Python environment using virtualenv (http://docs.python-guide.org/en/latest/dev/virtualenvs/). Install virtualenv with 'pip install virtualenv'. Then set your virtual environment up wth Python3 using this command: 'virtualenv -p python3 environmentname'. Now you should have a virtual environment ready and you can download the InteractiveNarrator and VisualNarrator into that directory.
Note that Interactive Narrator's python files are configured to be used in a virtual environment because of the shebang #!/usr/bin/env python

In the virtual environment you have created you should have the following file/folder structure:

```
your_virtualenvironment
│____bin
│____lib  
|____include
│____share
└───InteractiveNarrator
│   │
│   └───app
│       │   app.py
│       │   example_stories.txt
│       │   form.py
|       |   ....
│   
└───VisualNarrator
    │   run.py
    │
```
Note that you should place the Visual Narrator folder in the same directory as your
Interactive Narrator (InteractiveNarrator) is in.

Now change this line(21) in app.py and line(9) in post.py:
- sys.path.append('/home/gjslob/Documents/environments/inarrator/VisualNarrator')

**to:**
- sys.path.append('/path/on/your/computer/yourvirtualenvironment/VisualNarrator')

To tell Python where to look for de VisualNarrator package on your computer.


**Running the Project**

Linux:
1. open a terminal in your virtual environment directory
2. activate your virtual environment with 'source bin/activate'
3. change directory to the inwebapp folder with 'cd inwebapp'
4. run app.py with 'python app.py'
5. open your webbrowser and browse to http://127.0.0.1:5000/form
6. add identifiers for your company, company id, sprint name and sprint number(id)
7. submit the data and wait for the visualization to appear

To run the project with your own set of stories, change line 70 in app.py:
data = run.program('example_stories.txt')
to contain the filename of your own user story set located in the inwebapp folder
