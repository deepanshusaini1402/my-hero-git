from flask import Flask

app = Flask(__name__)

# function to read data from config file
def read_file():
    data = {}        
    section = ""  

    try:
        # open the file
        f = open("config.txt", "r")

        # read the file line by line
        for line in f:
            line = line.strip()   # remove spaces and new lines

            # skip empty lines
            if line == "":
                continue

            # if line starts and ends with [] then it's a section
            if line.startswith("[") and line.endswith("]"):
                section = line[1:-1]   # remove the brackets
                data[section] = {}     # make a new section in dictionary

            # if line contains = sign, it means key = value
            elif "=" in line and section != "":
                parts = line.split("=")
                key = parts[0].strip()
                value = parts[1].strip()
                data[section][key] = value   # store inside that section

        # close the file
        f.close()

    # if file is missing or cannot be opened
    except:
        print("Error: File not found or cannot read")

    # return the dictionary with all data
    return data


# read the config data when program starts
config_data = read_file()

# route to show the whole config file in json
@app.route("/config")
def show_all():
    return jsonify(config_data)

# route to show only one section like /config/Database
@app.route("/config/<name>")
def show_section(name):
    if name in config_data:
        return jsonify(config_data[name])
    else:
        return jsonify({"error": "Section not found"})

# start the flask web server
app.run(debug=True)
