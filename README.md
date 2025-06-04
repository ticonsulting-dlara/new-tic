# Nuevo sitio para TI Consulting

Este repositorio contiene una versión moderna del sitio web de [ticonsulting.cl](https://ticonsulting.cl/) implementado con **Python** y **Flask**. Incluye plantillas completas, una hoja de estilos y los scripts de integración para chat y agendamiento. El contenido es una base que puedes personalizar con tu información.

## Ejecutar localmente
1. Instala las dependencias (requiere Python 3.8 o superior):
   ```bash
   pip install -r requirements.txt
   ```
2. Inicia la aplicación:
   ```bash
   python app.py
   ```
3. Abre `http://localhost:5000` en tu navegador para ver el sitio.

## Estructura
- `app.py` aplicación Flask con las rutas principales
- `templates/` plantillas HTML que extienden `base.html`
- `assets/` archivos estáticos (CSS, imágenes y JavaScript)

El diseño utiliza la paleta de colores especificada y es responsive para diferentes dispositivos.
Los mensajes enviados desde el formulario de contacto se almacenan en `contacts.json`.

Incluye secciones de servicios, partners, clientes y un formulario de contacto con almacenamiento local.
