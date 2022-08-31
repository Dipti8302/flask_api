from app import app
import json

def test_get_all_books():
    response = app.test_client().get('/getdata')
    res = json.loads(response.data.decode('utf-8')).get("DATA")
    # assert type(res[0]) is list
    # assert type(res[1]) is dict
    assert res[0][0] == 'Aditi'
    assert res[0][1] == 'Dokhe'
    assert response.status_code == 200
    assert type(res) is list