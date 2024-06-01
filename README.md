# Инициализация boto3

```python
import boto3
bucket_name = "..."
s3 = boto3.client(
    "s3",
    endpoint_url="...",
    region_name="...",
    aws_access_key_id="...",
    aws_secret_access_key="...",
)
```

# Список бакетов
```python
for bucket in s3.list_buckets().get("Buckets", []):
    print(bucket["Name"])
```


# Список объектов в бакете
```python
for obj in s3.list_objects(Bucket=bucket_name).get("Contents", []):
    print(obj["Key"])
```


# Загрузка файла в бакет
```python
s3.upload_file(
    Filename="1.txt",  # Путь к файлу, который необходимо загрузить
    Bucket=bucket_name,  # Имя бакета, в который будет происходить загрузка
    Key="1.txt",  #  Имя, под которым файл будет сохранён в бакете
)
```

# Чтение файла
```python
data = s3.get_object(
    Bucket=bucket_name,  # Имя бакета, откуда нужно прочитать файл
    Key="1.txt",  # Имя файла в бакете
).get("Body")
if data is not None:
    print(data.read())
```

# Копирование файла
```python
s3.copy_object(
    CopySource={
        "Bucket": bucket_name,  # Имя бакета, из которого будет производиться копирование
        "Key": "1.txt",  # Имя файла, который будет скопирован
    },
    Bucket=bucket_name,  # Имя бакета, куда будет произведено копирование
    Key="1_copy.txt",  # Имя скопированного файла
)
```

# Удаление файла
```python
s3.delete_object(Bucket=bucket_name, Key="1_copy.txt")
```
