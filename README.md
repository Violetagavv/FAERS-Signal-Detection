Detección de Señales en FAERS: Ciencia de Datos en Farmacovigilancia

Este proyecto desarrolla un pipeline reproducible para detectar y priorizar señales de seguridad (combinaciones fármaco-evento) cuya frecuencia relativa excede la esperada bajo independencia, utilizando datos del FDA Adverse Event Reporting System (FAERS).

Objetivos
General: Desarrollar un pipeline de ciencia de datos para detectar señales de seguridad mediante medidas de desproporcionalidad y análisis temporal.
Específicos: Ingesta y limpieza de extractos trimestrales de FAERS.
    * Cálculo de medidas: PRR, ROR e IC.
    * Visualización interactiva mediante un tablero de control.


Lenguaje: Python (Pandas, SciPy)
Base de Datos: DuckDB (procesamiento eficiente de grandes volúmenes de datos)
Visualización: Dash/Streamlit
Control de versiones: Git/GitHub

Metodología
El proyecto se basa en el cálculo de medidas de desproporcionalidad a partir de tablas de contingencia,
aplicando correcciones estadísticas como la de Haldane y análisis de series de tiempo para identificar la emergencia de nuevas señales.
