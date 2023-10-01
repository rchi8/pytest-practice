import pytest
from src import sample_code

def get_json_data_mock(id):
    return {'name': 'さぷー'}


def test_get_suer_names(monkeypatch):
    monkeypatch.setattr(
        sample_code, 'get_json_data', get_json_data_mock
    )
    result = sample_code.get_user_names(['001', '009'])
    
    assert list(result.keys()) == ['001', '009']
    assert list(result.values()) == ['さぷー', 'さぷー']

def test_user_name_validation():
    with pytest.raises(ValueError) as e:
       # sample_code.user_name_validation(None)
       1/0
    assert str(e.value) == "名前が設定されていません"