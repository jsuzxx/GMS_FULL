from django.shortcuts import render

# Vista del login
def login_view(request):
    return render(request, 'dashboard/login.html')

# Vista del dashboard principal
def dashboard_view(request):
    datos = {
        'alertas_activas': 3,
        'nivel_promedio': 180,
        'estado_robot': 'Activo',
        'lecturas': [
            {'gas': 'CO2', 'nivel': 230, 'riesgo': 'Moderado'},
            {'gas': 'CH4', 'nivel': 120, 'riesgo': 'Bajo'},
            {'gas': 'NH3', 'nivel': 90, 'riesgo': 'Bajo'},
        ]
    }
    return render(request, 'dashboard/dashboard.html', datos)
