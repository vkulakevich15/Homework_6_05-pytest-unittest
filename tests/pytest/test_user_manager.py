import pytest
import allure

from src.user import User


@allure.feature("User Manager")
@allure.story("Add user")
def test_add_user(manager, user):
    manager.add_user(user)
    assert manager.count_users() == 1
    assert manager.get_user(user.id) == user


@allure.feature("User Manager")
@allure.story("Add user")
def test_add_user_duplicate_id(manager, user):
    manager.add_user(user)
    with pytest.raises(ValueError):
        manager.add_user(
            User(
                user_id= user.id,
                name= "qwert",
                age= 100,
                email= "qwert@gmail.com"
                )
        )

@allure.feature("User Manager")
@allure.story("Add user")
@pytest.mark.parametrize(
    "invalid_id",
    [
        "1",
        None,
        1.5
    ]
)
def test_invalid_id(manager, invalid_id):
    user = User(
        user_id= invalid_id,
        name= "Alice",
        age= 30,
        email= "alice@gmail.com")
    with pytest.raises(TypeError):
        manager.add_user(user)


@allure.feature("User Manager")
@allure.story("Add user")
@pytest.mark.parametrize(
    "name",
    [
        "",
        "A"
    ]
)
def test_invalid_name(manager, name):
    user = User(
        user_id= 1,
        name= name,
        age= 31,
        email= "alice31@gmail.com")
    with pytest.raises(ValueError):
        manager.add_user(user)


@allure.feature("User Manager")
@allure.story("Add user")
@pytest.mark.parametrize(
    "age",
    [
        -1,
        121
    ]
)
def test_invalid_age(manager, age):
    user = User(
        user_id= 1,
        name= "Alex",
        age= age,
        email= "alex@test.com")
    with pytest.raises(ValueError):
        manager.add_user(user)


@allure.feature("User Manager")
@allure.story("Add user")
@pytest.mark.parametrize(
    "email",
    [
        "test",
        "gmail.com"
    ]
)
def test_invalid_email(manager, email):
    user = User(
        user_id= 1,
        name= "Alex",
        age= 25,
        email= email)
    with pytest.raises(ValueError):
        manager.add_user(user)


@allure.feature("User Manager")
@allure.story("Get user")
def test_get_existing_user(manager, user):
    manager.add_user(user)


@allure.feature("User Manager")
@allure.story("Get user")
def test_get_missing_user(manager):
    assert manager.get_user(555) is None


@allure.feature("User Manager")
@allure.story("Remove user")
def test_remove_user(manager, user):
    manager.add_user(user)
    manager.remove_user(user.id)
    assert manager.get_user(user.id) is None
    assert manager.count_users() == 0


@allure.feature("User Manager")
@allure.story("Remove user")
def test_remove_missing_user(manager):
    with pytest.raises(ValueError):
        manager.remove_user(444)


@allure.feature("User Manager")
@allure.story("Get all users")
def test_get_all_users_empty(manager):
    assert manager.get_all_users() == []


def test_get_all_users_with_users(manager, user):
    manager.add_user(user)
    assert manager.get_all_users() == [user]

@allure.feature("User Manager")
@allure.story("Count users")
def test_count_users_empty(manager):
    assert manager.count_users() == 0


def test_count_users_with_users(manager, user):
    manager.add_user(user)
    assert manager.count_users() == 1