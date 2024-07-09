from flask import Flask, request, send_file, render_template
import your_image_generation_module  # Import the module that generates the image

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_image', methods=['GET'])
def generate_image():
    # Get input parameters from the request
    param1 = request.args.get('param1')
    # param2 = request.args.get('param2')
    
    # Call the function from your_image_generation_module to generate the image
    generated_image = your_image_generation_module.generate_image(param1)
    
    # Save the generated image to a file (e.g., 'generated_image.png')
    generated_image.save('generated_image.png')
    
    # Return the generated image as a response
    return send_file('generated_image.png', mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)
