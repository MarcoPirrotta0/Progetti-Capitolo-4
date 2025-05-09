from django.shortcuts import render
import io
import urllib, base64
import matplotlib.pyplot as plt
import pandas as pd
from django.shortcuts import render

# Create your views here.




def home(request):
    return render(request, 'home.html')

def plot_view(request):
    # Sample Pandas data
    df = pd.DataFrame({
        'x': range(1, 6),
        'y': [1, 4, 9, 16, 25]
    })

    # Create plot
    fig, ax = plt.subplots()
    ax.plot(df['x'], df['y'])
    ax.set_title("Example Plot")

    # Save plot to a bytes buffer
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Encode plot to base64 string
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    buffer.close()

    return render(request, 'plot.html', {'graph': graph})

