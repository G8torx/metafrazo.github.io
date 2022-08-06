from flask import Flask, render_template, request
import os
import openai

generated_text = ''

user_input = ''

#The current code language
input = ''
#The output language of the code 
output = ''

enabled = True

openai.api_key = os.getenv("Translate Programming Languages Key")

app = Flask(__name__) # Create an Instance

@app.route('/') # Route the Function
def main(): # Run the function 
  return render_template("index.html")

#Code for generating text
@app.route('/generate', methods=["POST", "GET"])#Methods post and get help send a response to a button to run this code
def generate():

  input = request.form.get('input')
  output = request.form.get("output")
  #this is the user prompt and the data is gathered from a prompt form/text box
  user_prompt = request.form['promptForm']

  #if the button method is == post then run the code for the ai
  if request.method == 'POST':
      #Checks if the bool enabled is true
      if enabled:
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"##### Translate this function from {input} into {output}\n### {input}\n    \n   {user_prompt}\n    \n### {output}",
        temperature=0,
        max_tokens=54,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["###"]
        )
        text = (response.choices[0].text)
      #if enabled is not true then display this in the text
      else:
        text = "The AI is not currently enabled."

      #Renders the generate.html
      return render_template('generate.html', generated_text=text, user_input=user_prompt) #set's the empty string gen_text to the ai gen text

app.run(host='0.0.0.0', port=5000, debug=True) # Run the Application (in debug mode)