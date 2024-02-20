from django.shortcuts import render

context = {
        "python" : {
            'id' : 1,
            'name' : 'Full stack using Python',
            'details': """ Full Stack Development using
                        Python
                        ITI Intensive Code Camp – (Full stack development using
                        Python) Specialization - is a product based program that
                        will empower you to learn how to build a complete
                        responsive web application using HTML, CSS, JavaScript,
                        Frontend frameworks like React or Angular, PostgreSQL,
                        Python, Django and Flask.
                    """,
            'courses' : ['HTML','CSS','JS','Python','Django']
        },
        "php" : {
            'id' : 2,
            'name' : 'Full stack using PHP',
            'details': """ Full Stack Development using PHP
                            ITI Intensive Code Camp – (Full stack development using
                            PHP) Specialization - is a product based program that 
                            will empower you to learn how to build a complete 
                            responsive web application using HTML, CSS, JavaScript,
                            Frontend frameworks like React or Angular, MySQL, PHP,
                            and Laravel
                    """,
            'courses' : ['HTML','CSS','JS','PHP','Laravel']
        },
        "mern" : {
            'id' : 3,
            'name' : 'Full stack using MERN',
            'details': """  Full Stack Development using MERN
                            ITI Intensive Code Camp – (Full stack development using
                            MERN) Specialization - is a product based program that
                            will empower you to learn how to build a complete
                            responsive web application using HTML, CSS, JavaScript,
                            Frontend frameworks like React, MongoDB, Express.js, Node.js,
                            and MERN stack.
                    """,
            'courses' : ['HTML','CSS','JS','Angular','React', 'Nodejs']
        }

    }

def home(request):
    return render(request, 'home.html')

def list_tracks(request):
   
    return render (request, 'list_tracks.html', {'tracks': context})


def track_details(request, name):
    if name in context:
        track_details = context[name]
        return render(request, "track_details.html",track_details)
    
    return render(request, "track_not_found.html")
    