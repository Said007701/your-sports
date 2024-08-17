from django.shortcuts import render

def start(element):
    copy_plan=[
        {"name":"Home","active":True},
        {"name":"Company","active":True},
        {"name":"About Sports","active":True},
        {"name":"Subscription","active":True},
        {"name":"Contact Us","active":True},
    ]
    copy_cont=[
        {"name":""}
    ]
    copy_fun={"copy_plan":copy_plan}
    return render(element,"index.html",copy_fun)

# Create your views here.
