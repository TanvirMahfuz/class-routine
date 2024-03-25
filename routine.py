from flask import Flask, render_template
import datetime

app = Flask(__name__)

class Class:
    def __init__(self, name, classname, time):
        self.TeacherName = name
        self.Name = classname
        self.Time = {
            "Saturday": time[0],
            "Sunday": time[1],
            "Monday": time[2],
            "Tuesday": time[3],
            "Wednesday": time[4]
        }

# Create instances of Class for different classes
class1 = Class("Sajjad Wahid", "Research Methodology", ["", "", "01:35", "09:30", "01:35"])
class2 = Class("Md Badrul Alam Miah", "Cryptography and Cyber Law", ["03:05", "11:15", "10:30", "", ""])
class3 = Class("Mst Nargis Akter", "Digital Image processing", ["", "", "11:15", "11:15", "2:20"])
class4 = Class("Md. Shahin Uddin", "Telecommunications Engineering", ["", "", "", "10:30", "09:00"])
class5 = Class("Mamun Al Babu Shikdar", "E-commerce and Web Programming", ["", "", "", "", "11:15"])

# Add the instances to the classes list
classes = [class1, class2, class3, class4, class5]

@app.route('/classes')
def get_classes():
    # Get the current day of the week
    current_day = datetime.datetime.now().strftime("%A")

    # Filter classes for the current day
    today_classes = []
    for c in classes:
        if c.Time[current_day] != "":
            today_classes.append({
                "Class": c.Name,
                "Teacher": c.TeacherName,
                "Time": c.Time[current_day]
            })

    # Render the HTML template with the class information
    return render_template('index.html',today_classes = today_classes)

if __name__ == '__main__':
    port = 5002
    app.run(debug=True,host='0.0.0.0', port=port)
