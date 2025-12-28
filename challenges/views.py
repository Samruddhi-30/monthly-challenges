from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

# Create your views here.



monthly_challenges = {
    "january": "Wake up 30 minutes earlier every day for one month",
    "february": "Write one page daily about thoughts, ideas, or learning",
    "march": "Exercise for at least 20 minutes every day",
    "april": "Learn and build one small project using a new technology",
    "may": "Read 10 pages of a book every day",
    "june": "Avoid social media during the first and last hour of the day",
    "july": "Solve one coding or logic problem daily",
    "august": "Practice mindfulness or meditation for 10 minutes daily",
    "september": "Improve communication by speaking confidently once every day",
    "october": "Create and share one useful piece of content every week",
    "november": "Practice gratitude by writing three things daily",
    "december": "Reflect on the year and plan clear goals for the next year"
}

def index(request):
    month = monthly_challenges.keys()
    list_items = ""
    for m in month:
        month_name = m.capitalize()
        month_path = reverse("month-name-challenge", args=[m])
        list_items+= f"<li><a href=\"{month_path}\">{month_name}</a></li>"
    

    response_data = f"""
        <h1>Welcomeee!!!</h1>
        <ul>
    
        {list_items}
  
        </ul>
"""
    return HttpResponse(response_data)


def month_by_num(request,month_num):
    months = list(monthly_challenges.keys())
    if month_num>len(months):
        return HttpResponseNotFound("Invalid month!!!")
    redirect_month = months[month_num-1] 
    redirect_path = reverse("month-name-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request , month_name):
    try:
        response_text = f"<h1>{monthly_challenges[month_name]}</h1>"
        return HttpResponse(response_text)
    except:
        return HttpResponseNotFound("This month has noo challenges, wowww")

    
        
