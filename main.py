import boto3


bucket_name = "42d58fa6-a90f41df-dd2b-4f45-a4a0-d1b0fbe98414"
s3 = boto3.client(
    "s3",
    endpoint_url="https://s3.timeweb.cloud",
    region_name="ru-1",
    aws_access_key_id="ZL9GVN7S4LSSCIE6607B",
    aws_secret_access_key="oYKga39dDJC5hW9B02Q03ThKMGdhtehg5w6HtQFg",
)

# Список бакетов
print("Список бакетов:")
for bucket in s3.list_buckets().get("Buckets", []):
    print(bucket["Name"])


# Список объектов в бакете
print("\nСписок объектов в бакете:")
for obj in s3.list_objects(Bucket=bucket_name).get("Contents", []):
    print(obj["Key"])


# Загрузка файла в бакет
s3.upload_file(
    Filename="1.txt",  # Путь к файлу, который необходимо загрузить
    Bucket=bucket_name,  # Имя бакета, в который будет происходить загрузка
    Key="1.txt",  #  Имя, под которым файл будет сохранён в бакете
)

# Чтение файла
print("\nСодержимое файла")
data = s3.get_object(
    Bucket=bucket_name,  # Имя бакета, откуда нужно прочитать файл
    Key="1.txt",  # Имя файла в бакете
).get("Body")
if data is not None:
    print(data.read())


# Копирование файла
s3.copy_object(
    CopySource={
        "Bucket": bucket_name,  # Имя бакета, из которого будет производиться копирование
        "Key": "1.txt",  # Имя файла, который будет скопирован
    },
    Bucket=bucket_name,  # Имя бакета, куда будет произведено копирование
    Key="1_copy.txt",  # Имя скопированного файла
)
print("\nОбъект успешно скопирован")


# Удаление файла
s3.delete_object(Bucket=bucket_name, Key="1_copy.txt")
print("\nОбъект успешно удалён")
