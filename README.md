# Home Credit Default Risk - Análisis y Predicción de Riesgo Crediticio

## Descripción del Proyecto

Este proyecto de aprendizaje automático utiliza la metodología CRISP-DM para analizar y predecir el riesgo de incumplimiento en préstamos de Home Credit. El proyecto procesa datos históricos de aplicaciones crediticias, información de bureau crediticio y historial de pagos, aplicando técnicas avanzadas de ciencia de datos y machine learning para desarrollar modelos predictivos de clasificación binaria.

## Autores

- Luis Salamanca
- Braihan Gonzales

## Fuente de Datos

Los datos provienen de la competencia **Home Credit Default Risk** de Kaggle. El dataset incluye múltiples tablas relacionadas que capturan:

- **application_train/test.csv**: Información principal de aplicaciones crediticias
- **bureau.csv**: Historial crediticio del bureau
- **bureau_balance.csv**: Balances mensuales del bureau
- **credit_card_balance.csv**: Balances de tarjetas de crédito
- **installments_payments.csv**: Historial de pagos por cuotas
- **POS_CASH_balance.csv**: Balances de créditos POS y cash
- **previous_application.csv**: Aplicaciones previas del cliente
- **sample_submission.csv**: Formato de envío para predicciones

### Características del Dataset

- **Aplicaciones principales**: 307,511 registros de entrenamiento + 48,744 de prueba
- **Formato**: Archivos CSV
- **Variable objetivo**: TARGET (0=pagó a tiempo, 1=dificultades de pago)
- **Features**: >100 variables numéricas y categóricas
- **Tablas auxiliares**: 7 tablas con información complementaria
- **Desbalance de clases**: ~8% de casos positivos (TARGET=1)
- **Fuente**: Kaggle Competition - Home Credit Default Risk

## Metodología CRISP-DM

### 1. Comprensión del Negocio
- **Objetivo**: Desarrollar modelos predictivos para evaluar riesgo crediticio
- **Casos de uso**: Aprobación de préstamos, determinación de tasas de interés, gestión de riesgo

### 2. Comprensión de los Datos
- **Análisis Exploratorio (EDA)**: Distribuciones, correlaciones, patrones de default
- **Calidad de datos**: Identificación de valores nulos, outliers, inconsistencias
- **Análisis de desbalance**: Estrategias para clases desbalanceadas

### 3. Preparación de los Datos
- **Limpieza**: Tratamiento de valores faltantes y outliers
- **Agregaciones**: Consolidación de tablas auxiliares
- **Ingeniería de características**: Creación de variables derivadas
- **Encoding**: Codificación de variables categóricas

### 4. Modelado
- **Algoritmos implementados**:
  - Regresión Logística
  - Random Forest
  - XGBoost
  - LightGBM

### 5. Evaluación
- **Métricas**: ROC-AUC, Precision, Recall, F1-Score
- **Validación**: División train/validation/test
- **Comparación de modelos**: Análisis de rendimiento

### 6. Despliegue
- **Contenedores Docker**: Orquestación completa del pipeline
- **Visualización**: Kedro Viz para monitoreo del pipeline
- **Notebooks**: Análisis interactivo con Jupyter Lab

## Arquitectura del Proyecto

### Estructura de Directorios

```
HomeCreditRisk/
├── data/                           # Gestión de datos por capas
│   ├── 01_raw/                     # Datos originales (CSV files)
│   ├── 02_intermediate/            # Datos procesados
│   ├── 03_primary/                 # Datos primarios limpios
│   ├── 04_feature/                 # Características engineered
│   ├── 05_model_input/             # Datos para entrenamiento
│   ├── 06_models/                  # Modelos entrenados
│   ├── 07_model_output/            # Predicciones
│   └── 08_reporting/               # Reportes y métricas
├── src/home_credit_risk/           # Código fuente
│   ├── pipelines/
│   │   ├── data_processing/        # Pipeline de procesamiento
│   │   └── data_science/           # Pipeline de ML
│   └── pipeline_registry.py       # Registro de pipelines
├── conf/                           # Configuraciones
│   ├── base/
│   │   ├── catalog.yml             # Catálogo de datasets
│   │   └── parameters.yml          # Hiperparámetros
│   └── local/                      # Configuraciones locales
├── notebooks/                      # Análisis exploratorio
├── tests/                          # Tests automatizados
└── docker-compose.yml             # Orquestación de servicios
```

## Comandos de Ejecución

### Usando Docker Compose (Recomendado)

#### Ejecución Completa del Pipeline
```bash
# Pipeline completo de ML
docker-compose up home-credit-ml

# Visualización del pipeline (http://localhost:4141)
docker-compose up kedro-viz

# Jupyter Lab para análisis (http://localhost:8888)
docker-compose up jupyter
```

### Ejecución Local

#### Pipeline Operations
```bash
# Pipeline completo
kedro run

# Solo procesamiento de datos
kedro run --pipeline data_processing

# Solo machine learning
kedro run --pipeline data_science

# Instalar dependencias
pip install -r requirements.txt
pip install -e .

# Visualizar pipeline
kedro viz
```

## Tecnologías y Herramientas

### Frameworks y Librerías
- **Kedro**: Orquestación de pipelines de ML
- **Pandas**: Manipulación y análisis de datos
- **Scikit-learn**: Algoritmos de machine learning
- **XGBoost**: Gradient boosting optimizado
- **LightGBM**: Gradient boosting eficiente
- **Category Encoders**: Codificación avanzada
- **Imbalanced-learn**: Manejo de clases desbalanceadas

### Infraestructura
- **Docker & Docker Compose**: Contenedorización y orquestación
- **Jupyter Lab**: Desarrollo interactivo
- **Kedro Viz**: Visualización de pipelines
- **pytest**: Framework de testing

## Métricas y Evaluación

### Métricas Implementadas
- **ROC-AUC** (Área bajo la curva ROC)
- **Precision** (Precisión)
- **Recall** (Sensibilidad)
- **F1-Score** (Media armónica de precisión y recall)

### Proceso de Validación
1. División estratificada manteniendo proporción de TARGET
2. Entrenamiento con validación cruzada
3. Optimización de umbrales de decisión
4. Evaluación final en conjunto de prueba
5. Análisis de importancia de características

## Casos de Uso

### Análisis Descriptivo
- Perfiles de riesgo por características demográficas
- Patrones de comportamiento crediticio
- Análisis de correlaciones con default
- Distribución de variables por grupo de riesgo

### Modelos Predictivos
- **Scoring crediticio**: Evaluación automática de solicitudes
- **Segmentación de riesgo**: Clasificación de clientes por nivel de riesgo
- **Políticas de aprobación**: Reglas de negocio basadas en modelos
- **Pricing diferenciado**: Tasas de interés según perfil de riesgo

## Requisitos del Sistema

### Dependencias Python
- Python >= 3.9
- Pandas >= 1.5.0
- Scikit-learn >= 1.1.0
- XGBoost >= 1.6.0
- LightGBM >= 3.3.0
- Kedro ~= 1.0.0

### Recursos Computacionales
- RAM: Mínimo 8GB (recomendado 16GB+)
- Almacenamiento: 10GB+ para datasets y modelos
- CPU: Multi-core recomendado para entrenamiento

---

*Desarrollado con Kedro Framework y metodología CRISP-DM para análisis profesional de riesgo crediticio.*
