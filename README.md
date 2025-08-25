Vale 🙌 entonces te preparo un **README.md actualizado**, pensado para que trabajes con archivos **`.npy`** (que es tu caso real), pero también dejando la opción de `.wav` si en algún momento los usas.

Aquí te va uno presentable:

---

```markdown
# 🎶 Análisis de Ondas Sonoras con Python

Este proyecto permite **cargar y analizar sonidos** usando Python.  
Las señales pueden estar en formato **`.npy`** (archivos de NumPy) o **`.wav`** (audio estándar).  
El programa genera gráficas en el **dominio del tiempo** y en el **dominio de la frecuencia** mediante la Transformada Rápida de Fourier (FFT).  

---

## 🚀 Funcionalidades
- Cargar archivos de audio (`.npy` o `.wav`).
- Graficar la señal en el tiempo.
- Aplicar FFT para obtener el espectro de frecuencias.
- Detectar la frecuencia fundamental y calcular:
  - Periodo
  - Frecuencia
  - Frecuencia angular

---

## 📂 Estructura del repositorio
```

├── analisis\_audio.py       # Script principal de análisis
├── ejemplos/               # Carpeta con audios de prueba
│   ├── nota\_flauta.npy
│   ├── nota\_guitarra.npy
│   └── nota\_piano.npy
└── README.md               # Este archivo

````

---

## ⚙️ Instalación

Clona el repositorio:
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
````

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Dependencias principales:

* `numpy`
* `matplotlib`
* `scipy`

---

## ▶️ Uso

### 🔹 1. Analizar un archivo `.npy`

Ejemplo con `nota_flauta.npy`:

```bash
python analisis_audio.py ejemplos/nota_flauta.npy
```

### 🔹 2. Analizar un archivo `.wav`

Ejemplo con `nota_flauta.wav`:

```bash
python analisis_audio.py ejemplos/nota_flauta.wav
```

El programa mostrará:

* La gráfica en el **tiempo**
* La gráfica del **espectro de frecuencias**
* La **frecuencia dominante** y sus características

---

## 📊 Ejemplo de salida

* **Oscilación en el tiempo**

![onda-tiempo](https://via.placeholder.com/600x200?text=Onda+en+el+Tiempo)

* **Espectro de frecuencia**

![onda-frecuencia](https://via.placeholder.com/600x200?text=Espectro+de+Frecuencia)

---

## 📌 Notas importantes

* En **GitHub Codespaces** no es posible usar micrófono en vivo.
  Por eso se recomienda trabajar con archivos `.npy` o `.wav`.
* Si quieres grabar desde tu PC local con micrófono, puedes usar `sounddevice` y guardar la grabación en `.npy` o `.wav` para analizarla después.

---

## ✍️ Autor

Proyecto realizado por **Jesús Pérez**
Estudiante de Física / Ingeniería — 2025

```

---

👉 ¿Quieres que también te prepare el `requirements.txt` exacto para que cualquier persona pueda clonar el repo y correr tu código sin instalar nada manualmente?
```
