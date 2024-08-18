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
    copy_tren=[
        {"img":"logo-1.png","text":"Sed vestibulum scelerisque urna, eu finibus leo facilisis sit amet. Proin id dignissim magna. Sed varius urna et pulvinar venenatis. ","active":True},
        {"img":"logo-3.png","text":"In efficitur in velit et tempus. Duis nec odio dapibus, suscipit erat fringilla, imperdiet nibh. Morbi tempus auctor felis ac vehicula. ","active":True},
    ]
    copy_tren1=[
        {"img":"logo-2.png","text":"Sed vestibulum scelerisque urna, eu finibus leo facilisis sit amet. Proin id dignissim magna. Sed varius urna et pulvinar venenatis. ","active":True},
        {"img":"logo-4.png","text":"In efficitur in velit et tempus. Duis nec odio dapibus, suscipit erat fringilla, imperdiet nibh. Morbi tempus auctor felis ac vehicula. ","active":True},
    ]
    copy_money=[
        {"name":"STUDENTS","money":"$","number":"8","month":"per month","text":"Personal License","btn":"purchase","active":True},
        {"name":"PROFESSIONAL","money":"$","number":"19","month":"per month","text":"Personal License Email Support","btn":"purchase","active":True},
    ]
    copy_money1=[
        {"name":"AGENCY","money":"$","number":"49","month":"per month","text":"1-12 Team Members Phone Support","btn":"purchase","active":True},
        {"name":"ENTERPRISE","money":"$","number":"79","month":"per month","text":"Unlimited Team Members 24/ 7 Phone Support","btn":"purchase","active":True},
    ]
    copy_social=[
        {"name":"fa fa-facebook-f"},
        {"name":"fa fa-twitter"},
        {"name":"fa fa-dribbble"},
        {"name":"fa fa-pinterest"},
    ]

    copy_fun={"copy_plan":copy_plan,"copy_cont":copy_cont,"copy_tren":copy_tren,"copy_tren1":copy_tren1,"copy_money":copy_money,"copy_money1":copy_money1,"copy_social":copy_social}
    return render(element,"index.html",copy_fun)

# Create your views here.
