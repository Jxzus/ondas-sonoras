import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
import os

# Parámetros de grabación
fs = 44100  # Frecuencia de muestreo
duration = 4  # Duración en segundos

def grabar_y_guardar(nombre_archivo):
    print("Grabando...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float64')
    sd.wait()
    print("Grabación finalizada.")
    np.save(nombre_archivo, audio)
    print(f"Grabación guardada como {nombre_archivo}.npy")
    return audio

def cargar_grabacion(nombre_archivo):
    return np.load(nombre_archivo)

def listar_grabaciones():
    return [f for f in os.listdir() if f.endswith('.npy')]

while True:
    print("\nOpciones de grabación:")
    print("1. Grabar nueva señal")
    print("2. Usar grabación existente")
    print("0. Salir")
    op = input("Opción: ")
    if op == "1":
        nombre = input("Nombre para guardar la grabación: ")
        audio = grabar_y_guardar(nombre + ".npy")
        break
    elif op == "2":
        grabaciones = listar_grabaciones()
        if not grabaciones:
            print("No hay grabaciones guardadas.")
            continue
        print("Grabaciones disponibles:")
        for i, g in enumerate(grabaciones):
            print(f"{i+1}. {g}")
        idx = int(input("Selecciona el número de la grabación: ")) - 1
        audio = cargar_grabacion(grabaciones[idx])
        print(f"Grabación {grabaciones[idx]} cargada.")
        break
    elif op == "0":
        print("Saliendo...")
        exit()
    else:
        print("Opción no válida. Intenta de nuevo.")

# --- Señal en el tiempo ---
t = np.linspace(0, duration, len(audio))

# --- Zoom para medir el periodo ---
zoom_start = 0.3  # segundos
zoom_end = 0.306  # segundos

# --- Transformada de Fourier ---
n = len(audio)
frequencies = np.fft.fftfreq(n, d=1/fs)
spectrum = np.fft.fft(audio[:,0])
mask = frequencies > 0

# --- Frecuencia dominante ---
dominant_freq = frequencies[mask][np.argmax(np.abs(spectrum[mask]))]
print(f"Frecuencia dominante: {dominant_freq:.2f} Hz")
print(f"Periodo: {1/dominant_freq:.4f} s")
print(f"Frecuencia angular: {2*np.pi*dominant_freq:.2f} rad/s")

# --- Reconstruir onda seno usando la frecuencia dominante ---
A = np.max(audio)  # Amplitud aprox
f0 = dominant_freq  # Frecuencia fundamental
t_zoom = t[(t >= zoom_start) & (t <= zoom_end)]
seno_ideal = A * np.sin(2 * np.pi * f0 * t_zoom)

def mostrar_menu():
    print("\nSelecciona la gráfica que deseas ver:")
    print("1. Oscilación en el tiempo")
    print("2. Zoom para medir el periodo")
    print("3. Espectro de Frecuencia")
    print("4. Comparación señal grabada vs seno reconstruido")
    print("5. Reproducir audio")
    print("0. Salir")

while True:
    mostrar_menu()
    opcion = input("Opción: ")
    if opcion == "1":
        plt.figure(figsize=(10,4))
        plt.plot(t, audio)
        plt.title("Oscilación en el tiempo")
        plt.xlabel("Tiempo [s]")
        plt.ylabel("Amplitud")
        plt.grid()
        plt.show()
    elif opcion == "2":
        plt.figure(figsize=(10,4))
        plt.plot(t, audio)
        plt.title("Zoom para medir el periodo")
        plt.xlabel("Tiempo [s]")
        plt.ylabel("Amplitud")
        plt.xlim(zoom_start, zoom_end)
        plt.grid()
        plt.show()
    elif opcion == "3":
        plt.figure(figsize=(10,4))
        plt.plot(frequencies[mask], np.abs(spectrum[mask]))
        plt.title("Espectro de Frecuencia")
        plt.xlabel("Frecuencia [Hz]")
        plt.ylabel("Amplitud")
        plt.grid()
        plt.show()
    elif opcion == "4":
        plt.figure(figsize=(10,4))
        plt.plot(t_zoom, audio[(t >= zoom_start) & (t <= zoom_end)], label="Señal real")
        plt.plot(t_zoom, seno_ideal, 'r--', label=f"Seno ideal {f0:.1f} Hz")
        plt.title("Comparación entre señal grabada y seno reconstruido")
        plt.xlabel("Tiempo [s]")
        plt.ylabel("Amplitud")
        plt.legend()
        plt.grid()
        plt.show()
    elif opcion == "5":
        print("Reproduciendo audio...")
        sd.play(audio, fs)
        sd.wait()
        print("Reproducción finalizada.")
    elif opcion == "0":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")