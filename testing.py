import pytest
from app import app

clients = app.test_client()

def test_home():
    resp = clients.get('/login')
    assert resp.status_code == 200

