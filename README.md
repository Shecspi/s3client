## Инициализация boto3

Для того, чтобы подключиться к хранилищу, необходимо создать клиента, передав ему настройки доступа хранилища. В последующем вся работа с хранилищем будет производиться через этот экземпляр клиента.

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

## Список бакетов

Список бакетов хранилища можно получить с помощью метода `list_buckets`, который возвращает следующий ответ:
```
{
    'Buckets': [
        {
            'Name': 'string',
            'CreationDate': datetime(2015, 1, 1)
        },
    ],
    'Owner': {
        'DisplayName': 'string',
        'ID': 'string'
    }
}
```

Поэтому, для получения списка бакетов необходимо обратиться к ключу `Buckets` возвращаемого словаря и к ключу `Name` каждого бакета.

```python
for bucket in s3.list_buckets().get("Buckets", []):
    print(bucket["Name"])
```


## Список объектов в бакете

Список бакетов хранилища можно получить с помощью метода `list_buckets`, который возвращает следующий ответ:
```
{
    'IsTruncated': True|False,
    'Marker': 'string',
    'NextMarker': 'string',
    'Contents': [
        {
            'Key': 'string',
            'LastModified': datetime(2015, 1, 1),
            'ETag': 'string',
            'ChecksumAlgorithm': [
                'CRC32'|'CRC32C'|'SHA1'|'SHA256',
            ],
            'Size': 123,
            'StorageClass': 'STANDARD'|'REDUCED_REDUNDANCY'|'GLACIER'|'STANDARD_IA'|'ONEZONE_IA'|'INTELLIGENT_TIERING'|'DEEP_ARCHIVE'|'OUTPOSTS'|'GLACIER_IR'|'SNOW'|'EXPRESS_ONEZONE',
            'Owner': {
                'DisplayName': 'string',
                'ID': 'string'
            },
            'RestoreStatus': {
                'IsRestoreInProgress': True|False,
                'RestoreExpiryDate': datetime(2015, 1, 1)
            }
        },
    ],
    'Name': 'string',
    'Prefix': 'string',
    'Delimiter': 'string',
    'MaxKeys': 123,
    'CommonPrefixes': [
        {
            'Prefix': 'string'
        },
    ],
    'EncodingType': 'url',
    'RequestCharged': 'requester'
}
```

Поэтому, для получения списка объектов в бакете необходимо обратиться к ключу `Contents` возвращаемого словаря и к ключу `Key` каждого бакета.

```python
for obj in s3.list_objects(Bucket=bucket_name).get("Contents", []):
    print(obj["Key"])
```


## Загрузка файла в бакет
```python
s3.upload_file(
    Filename="1.txt",  # Путь к файлу, который необходимо загрузить
    Bucket=bucket_name,  # Имя бакета, в который будет происходить загрузка
    Key="1.txt",  #  Имя, под которым файл будет сохранён в бакете
)
```

## Чтение файла
```python
data = s3.get_object(
    Bucket=bucket_name,  # Имя бакета, откуда нужно прочитать файл
    Key="1.txt",  # Имя файла в бакете
).get("Body")
if data is not None:
    print(data.read())
```

## Копирование файла
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

## Удаление файла
```python
s3.delete_object(Bucket=bucket_name, Key="1_copy.txt")
```
