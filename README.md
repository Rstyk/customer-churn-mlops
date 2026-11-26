
# Customer Churn MLOps

## Мета проєкту

Створення базового MLOps-проєкту для прогнозування
відтоку клієнтів (Customer Churn) за допомогою
машинного навчання.

## Джерело даних

Використовується набір даних Telco Customer Churn
із платформи Kaggle.

https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Файл даних: data/raw/churn.csv

## Структура проєкту

- data/raw/ — початкові дані
- data/processed/ — оброблені дані
- models/ — збережені моделі
- notebooks/ — експерименти
- reports/ — результати навчання
- src/ — програмний код
- tests/ — тести
- requirements.txt — список бібліотек

## Встановлення залежностей

pip install -r requirements.txt

## Запуск моделі

python src/train.py

## Результати навчання

- Accuracy: 0.7637
- Precision: 0.7303
- Recall: 0.1738
- F1-score: 0.2808
- ROC-AUC: 0.8195

## Висновок

У результаті роботи створено MLOps-проєкт
для прогнозування відтоку клієнтів.

Підготовлено дані, навчено базову модель
логістичної регресії та отримано метрики якості.

Модель і результати збережено в окремих файлах.
Отримані показники можна використовувати для
подальшого вдосконалення моделі.

## Лабораторна робота №2

### Валідація даних

Для запуску перевірки даних:

```bash
python src/validate_data.py
```

Результати валідації:
- passed — дані успішно пройшли перевірку.
- failed — у даних виявлено помилки.

Звіт валідації:
`reports/data_validation_report.json`

### Версіонування датасету

Для створення підготовленої версії датасету:

```bash
python src/version_data.py
```

Підготовлений датасет:
`data/processed/churn_v1.csv`

Файл метаданих:
`data/processed/churn_v1_metadata.json`

### Навчання моделі

Для запуску навчання моделі:

```bash
python src/train.py
```

Модель використовує перевірений та підготовлений датасет версії v1.

## Лабораторна робота №3

### Запуск MLflow

```powershell
python -m mlflow server --backend-store-uri sqlite:///mlflow.db --host 127.0.0.1 --port 5000
```

Інтерфейс MLflow доступний за адресою:
http://127.0.0.1:5000

### Запуск експериментів

Логістична регресія:

```powershell
python src/train_experiments.py --model-type logistic_regression
```

Випадковий ліс (Random Forest):

```powershell
python src/train_experiments.py --model-type random_forest
```

### Збереження результатів

Параметри та метрики експериментів зберігаються
у локальній базі mlflow.db, а артефакти — у mlartifacts/.

Результати можна переглянути в розділі Experiments.

### Реєстр моделей

За метрикою ROC-AUC обрано модель Random Forest.

Модель зареєстровано під назвою
CustomerChurnClassifier, версія 1.

Переглянути модель можна в розділі Model registry.

Результати порівняння моделей збережено у
reports/model_selection.md.

