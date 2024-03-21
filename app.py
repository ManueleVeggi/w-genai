from flask import Flask, render_template, request, url_for, flash, redirect
# Notes on the imports:
# The global request object to access incoming request data that will be submitted via the HTML form you built in the last step.
# The url_for() function to generate URLs.
# The flash() function to flash a message when a request is processed (to inform the user that everything went well, or to inform them of an issue if the submitted data is not valid).
# The redirect() function to redirect the client to a different location.

# 1. Create an instance of the Flask class
app = Flask(__name__) # __name__ holds the name of the current module and tells the app where to look for templates, static files, and so on.

# 2. Initialize the dictionary with the images and prompts
img_storage = {
    True: "static/media/stable_painter.jpeg",
    False: ""
}

# State ancillary function
def get_image(prompt):
    return img_storage["paint" in prompt]

# 3. Define the route and the view function
# this is a decorator that turns a Py function into a Flask view function: the return value of the function is the response to the request.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    key = request.form['prompt']
    image_path = get_image(key)
    return render_template('index.html', image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)

# Up to now, the complexity on the code does not justify the implementation of a Flask app.
# On the contrary, this skeleton and the implementation of a GenAI algorithm in the notebook,
# may be combined to create a working web app: the function to generate the image will indeed
# replace the current get_image function

# For now the biggest issue is to find an online GPU to run the GenAI algorithm:
# a local deployment is not feasible due to the lack of computational resources
# and is not compatible with the requirements of the project.