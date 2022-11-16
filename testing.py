import pytest
from app import app

client = app.test_client()

def test_home(client):
    resp = client.get('/login')
    assert resp.status_code == 200

