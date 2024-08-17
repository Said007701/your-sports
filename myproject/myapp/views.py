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
        {"name":"Riding Mountain Bike","text":"Aenean cursus imperdiet nisl id fermentum. Aliquam pharetra dui laoreet vulputate dignissim. Sed id metus id quam auctor molestie eget ut augue.","img":"graph-04.svg","active":True},
        {"name":"Volley Ball Intense Training","text":"Maecenas eu dictum felis, a dignissim nibh. Mauris rhoncus felis odio, ut volutpat massa placerat ac. Curabitur dapibus iaculis mi gravida luctus. Aliquam erat volutpat. ","img":"graph-03.svg","active":True},
        {"name":"Learn Surfing From Experts","text":"Maecenas eu dictum felis, a dignissim nibh. Mauris rhoncus felis odio, ut volutpat massa placerat ac. Curabitur dapibus iaculis mi gravida luctus. Aliquam erat volutpat. ","img":"graph-02.svg","active":True},
        {"name":"Archers Club","text":"Maecenas eu dictum felis, a dignissim nibh. Mauris rhoncus felis odio, ut volutpat massa placerat ac. Curabitur dapibus iaculis mi gravida luctus. Aliquam erat volutpat. ","img":"graph-01.svg","active":True},
    ]
   

    copy_fun={"copy_plan":copy_plan,"copy_cont":copy_cont}
    return render(element,"index.html",copy_fun)

# Create your views here.
