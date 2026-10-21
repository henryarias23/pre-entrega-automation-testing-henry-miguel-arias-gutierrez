# Pre-Entrega Automation Testing - SauceDemo
Este repositorio contiene la solución para la pre-entrega de automatización de pruebas, enfocada en validar los flujos críticos de la plataforma de comercio electrónico [SauceDemo](https://www.saucedemo.com/). El proyecto implementa buenas prácticas de testing utilizando un enfoque estructurado con **Python**, **Selenium WebDriver** y **PyTest**

## 📌 Propósito del Proyecto
El objetivo principal es validar los flujos fundamentales de la plataforma web:
- **Automatización de Login:** 
    Validación de acceso con credenciales válidas (usuario estándar y contraseña) para comprobar el acceso exitoso al sistema.
- **Navegación e Inventario:** 
    Verificación de la carga correcta de la página de productos tras el inicio de sesión;
    Comprobación de elementos clave de la interfaz, como el título de la sección de inventario y la visualización correcta de los artículos disponibles.
- **Interacción con Productos:** 
    Agregar items al carrito, verificación del contador del carrito y navegación al carrito de compras.

---

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python
- **Framework de Testing:** PyTest
- **Automatización Web:** Selenium WebDriver
- **Generación de Reportes:** pytest-html
- **Control de Versiones:** Git & GitHub

---

## 📦 3. Instrucciones de Instalación de Dependencias

Sigue estos pasos en tu terminal (CMD, PowerShell o terminal de VS Code) tras a ver clonado el repositorio, Para preparar el entorno de desarrollo e instalar los paquetes necesarios para la automatización:

- Apertura de la Terminal Integrada
Para iniciar la configuración del entorno, abre la terminal en Visual Studio Code utilizando el siguiente atajo de teclado:

Ctrl + ñ

ejecuta los siguientes comandos en el orden indicado:

- Instalación de PyTest (Framework de Pruebas)
Instala el framework de pruebas y verifica que la instalación haya sido exitosa comprobando su versión:

pip install pytest
pytest --version


- Instala la extensión de reportes en HTML y consulta la información del paquete instalado:

pip install pytest-html
pip show pytest-html


- Instalación de Selenium: Instala la librería principal de automatización web:

pip install selenium


- Instalación de WebDriver Manager: Instala el gestor automático de controladores:

pip install webdriver-manager

🚀 Comando para Ejecutar las Pruebas

Para ejecutar la suite de pruebas y generar el reporte HTML de forma simultánea, ejecuta el siguiente comando en la raíz del proyecto:

pytest -v --html=reporte.html