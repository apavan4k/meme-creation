from django.shortcuts import render, get_object_or_404, redirect
from .models import Meme
from .forms import MemeForm

# List all memes
def meme_list(request):
    memes = Meme.objects.all().order_by('-created_at')
    return render(request, 'create.html', {'memes': memes})

# Create new meme
def meme_create(request):
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MemeForm()
    return render(request, 'create.html', {'form': form})

# Meme details
def meme_detail(request, pk):
    meme = get_object_or_404(Meme, pk=pk)
    return render(request, 'detail.html', {'meme': meme})

# Edit meme
def meme_edit(request, pk):
    meme = get_object_or_404(Meme, pk=pk)
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES, instance=meme)
        if form.is_valid():
            form.save()
            return redirect('meme_detail', pk=meme.pk)
    else:
        form = MemeForm(instance=meme)
    return render(request, 'edit.html', {'form': form})
