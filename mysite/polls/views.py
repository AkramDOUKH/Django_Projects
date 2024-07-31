from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Choice, Question
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Choice, Question

def index(request):
# Create your views here.
    return HttpResponse("""<a href = "2">What is the Answer to the Ultimate Question of Life, the Universe, and Everything?</a>""")
def owner(request):
    return HttpResponse("Hello, world. 506e2c43 is the polls index.")
def detail(request,question_id):
    q = Question.objects.get(pk=question_id)
    c = q.choice_set.filter(choice_text__startswith="42")
    resp = c[0].choice_text
    return HttpResponse("""<p>The Answer to the Ultimate Question is: """ + resp + """.</p>""")

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

