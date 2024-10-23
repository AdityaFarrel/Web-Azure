from flask import Flask, render_template

app = Flask(__name__)

# Data pribadi untuk empat orang
data_diri = [
    {
        'nama': 'Faris Nauval Marzuqi',
        'nim': '22.83.0801',
        'prodi': 'Teknik Komputer',
        'hobi': 'Master Fishing',
        'deskripsi': 'Mr.Nobody',
        'foto': 'images/foto1.jpg'
    },
    {
        'nama': 'Rayyan Abdie Azzaky',
        'nim': '22.83.0811',
        'prodi': 'Teknik Komputer',
        'hobi': 'Sleep All The Time.',
        'deskripsi': 'Hidup Seperti Larry',
        'foto': 'images/foto2.jpg'
    },
    {
        'nama': 'Aditya Farrel Firdaus',
        'nim': '22.83.0825',
        'prodi': 'Teknik Komputer',
        'hobi': 'Go For A Walk',
        'deskripsi': 'Stay Halal Brother.',
        'foto': 'images/foto3.jpg'
    },
    {
        'nama': 'Tri Azani',
        'nim': '22.83.0764',
        'prodi': 'Teknik Komputer',
        'hobi': 'Pro Fishing',
        'deskripsi': 'Its all Just About The Time',
        'foto': 'images/foto4.jpg'
    }
]

@app.route('/')
def home():
    return render_template('index.html', data_list=data_diri)

if __name__ == '__main__':
    app.run(debug=True)
