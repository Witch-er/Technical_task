import requests
import json
##case-1
id=2001
data_post = {
  "id": 2001,
  "category": {
    "id": 1,
    "name": "asdasd"
  },
  "name": "doggie",
  "photoUrls": [
    "sdsfng"
  ],
  "tags": [
    {
      "id": 2,
      "name": "tdsfng"
    }
  ],
  "status": "available"
}
data_header = {"user-agent": "Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666"}
def test_first_step_case_1(): ##1.Добавить нового питомца в магазин
    r = requests.post("https://petstore.swagger.io/v2/pet", json=data_post, headers=data_header)
    assert r.status_code == 200
    print(r.json())
def test_second_step_case_1(): ##2.Проверить, что питомец добавлен
    re = requests.get("https://petstore.swagger.io/v2/pet/"+str(id), headers=data_header)
    assert re.status_code == 200
    print(re.json())
def test_third_step_case_1(): ##3.Удалить питомца
    res=requests.delete("https://petstore.swagger.io/v2/pet/"+str(id), headers=data_header)
    assert res.status_code==200
    print(res.json())
def test_four_step_case_1(): ##4.Проверить, что питомца больше не существует
    resp=requests.get("https://petstore.swagger.io/v2/pet/"+str(id), headers=data_header)
    assert resp.status_code == 404
    print(resp.json())
    print("CASE-1-PASSED")
##case-2
username="user2"
data_user={
  "id": 1,
  "username": "user2",
  "firstName": "Buser",
  "lastName": "Resub",
  "email": "sdfsdf",
  "password": "dfgddfg",
  "phone": "werewr",
  "userStatus": 1
}
put_username="user1"
put_data={
  "id": 1,
  "username": "user1",
  "firstName": "Buser",
  "lastName": "Resub",
  "email": "sdfsdf",
  "password": "dfgddfg",
  "phone": "werewr",
  "userStatus": 1
}
def test_first_step_case_2():##1.Создать пользователя
    r = requests.post("https://petstore.swagger.io/v2/user", json=data_user, headers=data_header)
    assert r.status_code == 200
    print(r.json())
def test_second_step_case_2(): ##2.Получить данные пользователя
    re = requests.get("https://petstore.swagger.io/v2/user/" + username, headers=data_header)
    assert re.status_code == 200
    print(re.json())
def test_third_step_case_2():##3.Изменить имя пользователя
    res = requests.put("https://petstore.swagger.io/v2/user/" + username, json=put_data, headers=data_header)
    assert res.status_code == 200
    print(res.json())
def test_four_step_case_2():##4.Проверить, что имя изменилось
    resp = requests.get("https://petstore.swagger.io/v2/user/" + put_username, headers=data_header)
    assert resp.status_code == 200
    print(resp.json())
    print("CASE-2-PASSED")
def test_five_step_case_2():##5.Удалить пользователя
    respo = requests.delete("https://petstore.swagger.io/v2/user/" + put_username, headers=data_header)
    assert respo.status_code == 200
    print(respo.json())
    print("User deleted.")

