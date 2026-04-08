# Observaciones generales y temario del curso

<p float="left">
xkcd comic: Trained a Neural Net

  <img src="https://imgs.xkcd.com/comics/trained_a_neural_net.png" height="485" />

"It also works for anything you teach someone else to do. ``Oh yeah, I trained a pair of neural nets, Emily and Kevin, to respond to support tickets."
  Source: https://xkcd.com/2173/
</p>

<p float="left">
  <img
    src="https://imgs.xkcd.com/comics/trained_a_neural_net.png"
    height="485"
    alt="xkcd comic: Trained a Neural Net"
    title="It also works for anything you teach someone else to do. `Oh yeah, I trained a pair of neural nets, Emily and Kevin, to respond to support tickets.`"
  />
</p>

## Citas para preguntas
Únicamente solicitándolas previamente, ya sea por correo electrónico o antes/después de la clase.

## Exámenes, talleres y fechas
El curso se evaluará mediante exámenes y talleres prácticos (que deben ser expuestos ante el público).

### Exámenes:
* **Examen 1:** 20%
  * Parte 1 (50%):
    * Fecha (semana 3):
      * Jueves Abril 24, 2025
    * Tema: Se harán dos preguntas:
      * Una de álgebra lineal o de teoría de probabilidades.
      * Otra del libro xxx:
          - Capítulo 3: xxx
          - Capítulo 4: xxx

  * Parte 2 (50%):
    * Fecha (semana 6):
      * Jueves Mayo 15, 2025
    * Tema: Se harán dos preguntas:
      * Una de cálculo vectorial.
      * Otra del libro xxx:
          - Capítulo 3: xxx
          - Capítulo 4: xxx

* **Examen 2:** 17%
    * Fecha (semana 9):
      * Jueves Mayo 29, 2025.
    * Tema:
      * Del libro xxx:
          - Capítulo 3: xxx
          - Capítulo 4: xxx
      * Todos los códigos de programación asociados.
      * Ver cuestionario de estudio para el examen 2.

* **Examen 3:** 17%
    * Fecha (semana 12):
      * Jueves Junio 26, 2025
    * Tema: 
      * Del libro xxx:
          - Capítulo 3: xxx
          - Capítulo 4: xxx
      * Todos los códigos de programación asociados.
      * Ver cuestionario de estudio para el examen 3.

* **Examen 4:** 16%
    * Fecha (semana 16):
      * Jueves Julio 24, 2025
    * Tema: 
      * Del libro xxx:
          - Capítulo 3: xxx
          - Capítulo 4: xxx
      * Todos los códigos de programación asociados.
      * Ver cuestionario de estudio para el examen 4.

* **Talleres:** 30% 
* Se harán 2 talleres prácticos, que deberán ser expuestos ante el público.
* Las fechas de entrega de los talleres serán:
    * Taller 1: xxx
    * Taller 2: xxx

En los exámenes siempre se preguntará: teoría, demostraciones, ejercicios numéricos y ejercicios de programación.

<code style="color: #ff0000;">Se permite para los exámenes, que el profesor indique, traer una hoja tamaño carta en la cual ustedes pueden escribir (POR UN SOLO LADO) todas las fórmulas y comandos de PYTHON que deseen. En la hoja no se pueden ni escribir programas, ni textos explicativos, ni se pueden escribir demostraciones. Dicha hoja debe ser de elaboración personal (no se pueden traer las hojas hechas por compañeros de este o semestres pasados) y debe hacerse a mano (se prohíbe explícitamente traer fotocopias/impresiones/reducciones).</code>

## Descripción de la asignatura y objetivos de aprendizaje

En este curso se hará una introducción a el aprendizaje automático (machine learning) con énfasis en aplicaciones a la ingeniería civil. Se cubrirán los fundamentos teóricos de los modelos de aprendizaje automático, así como técnicas de entrenamiento, regularización y arquitecturas como los perceptrones multicapa y las redes neuronales convolucionales y recurrentes. Se enfatizará el uso de Python y bibliotecas populares como NumPy, pandas, Matplotlib, scikit-learn y PyTorch o TensorFlow. 

Se realizarán aplicaciones reales en áreas como monitoreo de salud estructural, predicción de resistencia de materiales, análisis de series temporales en tráfico y recursos hídricos, detección de daños por imágenes, redes neuronales informadas por física para modelado de procesos físicos, aproximación eficiente de simulaciones costosas computacionalmente, entre otras aplicaciones relevantes para la ingeniería civil.

La materia se desarrollará mediante clases magistrales, complementadas con el análisis de casos prácticos en ingeniería civil.

<!---
Además, se explorarán aplicaciones prácticas en áreas como:
* Predicción de la resistencia del hormigón, asentamientos o tendencias de volumen de tráfico a partir de datos limitados.
* Monitorización del estado estructural mediante sensores de vibración o imágenes de fisuras.
* Predicción de series temporales de caudal fluvial, densidad de tráfico o respuestas estructurales.
* Detección de daños en infraestructuras mediante imágenes.
* Redes neuronales basadas en la física para el modelado de procesos físicos en ingeniería civil.
* Predicción del factor de seguridad o probabilidad de fallo a partir del perfil del suelo, el ángulo de la pendiente y el historial de precipitaciones.
* Predicción del IRI (Índice Internacional de Rugosidad) o la densidad de fisuras a partir de datos de sensores (acelerómetros) o estudios basados ​​en imágenes.
* Aproximación de resultados de análisis de elementos finitos (FEM) costosos (p. ej., desplazamiento máximo, puntos críticos de tensión) mediante redes neuronales para abaratar los análisis repetidos. 
* Predicción de retrasos en autobuses o trenes y aglomeraciones de pasajeros mediante datos históricos, información meteorológica y señales GPS en tiempo real para optimizar la planificación y las rutas.
* Combinación de datos geoespaciales (altitud, uso del suelo, tipo de suelo, precipitaciones) con aprendizaje automático para crear mapas de alta resolución que identifiquen las zonas con mayor riesgo de inundaciones repentinas.
--->

Se espera que al final del curso, el estudiante esté en capacidad de:
* Identificar y explicar los fundamentos teóricos de los modelos de aprendizaje automático.
* Identificar y formular problemas de ingeniería civil (estructural, geotécnica, transporte, hidráulica) como tareas de aprendizaje automático.
*Implementar y entrenar modelos de regresión lineal, perceptrones multicapa (MLPs), redes neuronales convolucionales (CNNs) y recurrentes (RNNs/LSTM/GRU) en Python, aplicándolos a datos reales de sensores, imágenes o series temporales.
* Aplicar técnicas de optimización (backpropagation, descenso de gradiente, Adam), regularización (L1/L2, dropout, normalización) y prevención de sobreajuste para mejorar la generalización de modelos en escenarios de ingeniería con datos limitados o ruidosos.
* Evaluar críticamente los resultados obtenidos y comunicar sus hallazgos de manera efectiva.

La materia se desarrollará mediante clases magistrales.

## Contenido programático

### 0. Repaso de diferentes temas de álgebra lineal, cálculo vectorial y teoría de probabilidades.

Cada estudiante debe repasar por cuenta propia los siguientes temas:
#### Repaso de álgebra lineal (teoría y ejercicios de aplicación)
* Producto punto, producto cruz (con todas las propiedades que aparecen en el apéndice de las notas)
* Norma de un vector
* Matrices
* Valores y vectores propios
* Espacios vectoriales
* Vectores linealmente dependientes/independientes
* Bases
* Planos y líneas rectas
* Matrices ortogonales, simétricas, definidas positivas.

#### Repaso de cálculo vectorial (teoría y ejercicios de aplicación)
* Gradiente
* Matriz jacobiana y jacobiano
* Optimización de funciones multivariadas sin restricciones
* Optimización de funciones multivariadas con restricciones de igualdad (multiplicadores de Lagrange)
* Regla de la cadena (se estudió en cálculo univariado y en cálculo vectorial)

#### Repaso de teoría de probabilidades (teoría y ejercicios de aplicación)
* Variables aleatorias discretas y continuas
* Función de distribución acumulada
* Función de densidad de probabilidad
* Esperanza matemática, varianza y desviación estándar
* Distribuciones de probabilidad: uniforme, normal, Bernoulli
* Método de la máxima verosimilitud (maximum likelihood method)

### 1. Introduction to machine learning
* Overview of ML in civil engineering (structural, geotechnical, transport, water, structural health monitoring).
* Types of learning: supervised, unsupervised, semi‑supervised; reinforcement learning.
* Neural networks and deep learning
* Datasets
* Features

### 2. Linear regression
* Simple and multiple linear regression
* Polynomial regression
* Training, validation, testing sets
* Loss functions for regression
* Least squares
* LMS algorithm
* Overfitting vs. Underfitting
* Bias-variance trade-off
* Model selection
* Limitations of linear models
* Applications of linear regression in civil engineering

### 3. Multilayer perceptrons
* History of the MLPs
* Universal approximation theorem
* Architecture of the MLP: activation functions, hidden layers, weights and bias
* Loss functions for regression and classification
* Training of MLPs
* Data preprocessing
* Weight initialization
* Limitations of MLPs
* Applications of MLPs in civil engineering

### 4. Training and backpropagation
* Training as an optimization problem
* Backpropagation
* Automatic differentiation
* Batch learning 
* Online learning
* Learning curve
* Learning rate and schedulers
* Momentum
* Optimization methods (gradient descent, RMSProp, AdaGrad, Adam, etc)
* Vanishing and exploding gradients
* Hyperparameter tuning
* Physics‑informed neural networks
* Applications of training techniques in civil engineering

### 5. Regularization and other techniques to improve generalization
* Regularization L1 (Lasso)
* Regularization L2 (Ridge, Tikhonov, or weight decay)
* Early stopping
* Data augmentation
* Dropout
* Residual connections
* Normalization layers
* Batch normalization
* Layer normalization
* Applications of regularization techniques in civil engineering

### 6. Convolutional neural networks
* Architecture of a CNN: convolutional, pooling and fully connected layers
* Channels of an image
* Most popular CNNs: LeNet, AlexNet, VGG-16, ResNet, etc.
* ImageNet dataset
* Normalization layer methods for CNNs
* Object detection, YOLO family
* Semantic segmentation
* Limitations of CNNs
* Applications of CNNs in civil engineering

### 7. Recurrent neural networks
* NARX and Elman networks as precursors to RNNs
* Training methods (BPTT)
* Vanishing and exploding gradients
* Gated RNNs: LSTM and GRU
* Stacked and bidirectional RNNs
* Limitations of RNNs
* Introduction to transformers and attention mechanisms
* Applications of RNNs in civil engineering

<!---
### 11. Applications of machine learning in engineering

### 12. Ethical considerations in machine learning
--->

## Bibliografía básica

Ver en la página [Recursos](02_-_resources.md)


## Otras observaciones que se quieren dejar por escrito:

### Falta a los exámenes
Siempre que usted falte a un examen, debe haber algún documento que lo exonere de dicha inasistencia. Cuando usted por algún motivo de fuerza mayor no pueda asistir al examen, usted debe avisarle al profesor con anterioridad ya sea personalmente o por correo. En esos casos en lo posible, debe demostrarlo. Por ejemplo: si le tocó viajar a su pueblo esa semana porque algo sucedió un evento familiar de trascendencia, entonces una forma de certificar que usted viajó son los tiquetes de ida y vuelta a su pueblo. Sin una excusa o una notificación previa no se repetirán los exámenes y usted tendrá como nota un cero.

### Fraude en los exámenes o trabajos
Estos se penalizarán así:
* Nota cero en el trabajo/examen en cuestión.
* Carta al Consejo de Facultad reportando el suceso.
<!---
* Se pierden adicionalmente todos los privilegios que se tienen de una calificación con notas mayores a 5.0 en todas las notas obtenidas en el semestre, los puntos de la WIKI y cualquier bonificación adicional de notas que el profesor decida otorgar al grupo.
--->

### "Minuciosamente" en los exámenes
En todos los exámenes se debe relacionar con palabras las fórmulas y motivar físicamente el por qué de un procedimiento o fórmula (es decir, se debe escribir la explicación suponiendo que usted está escribiendo un libro). Si no se hace esto, se le rebajará en ese punto en particular el 50% de la nota.
