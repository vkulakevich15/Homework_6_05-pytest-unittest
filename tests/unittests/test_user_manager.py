import unittest
import allure

from src.user import User
from src.user_manager import UserManager


@allure.feature("User Manager")
class TestUserManager(unittest.TestCase):

    def setUp(self):
        self.manager = UserManager()

        self.user = User(
            user_id=1,
            name="Alex",
            age=25,
            email="alex@test.com"
        )

    def tearDown(self):
        self.user = None
        self.manager = None

    @allure.story("Add user")
    @allure.title("Add valid user")
    def test_add_user(self):
        self.manager.add_user(self.user)
        self.assertEqual(self.manager.count_users(), 1)

    @allure.story("Add user")
    @allure.title("Duplicate id raises ValueError")
    def test_add_user_duplicate_id(self):
        self.manager.add_user(self.user)
        with self.assertRaises(ValueError):
            self.manager.add_user(self.user)

    @allure.story("Add user")
    @allure.title("Invalid id type raises TypeError")
    def test_add_user_invalid_id_type(self):
        self.user.id = "1"
        with self.assertRaises(TypeError):
            self.manager.add_user(self.user)

    @allure.story("Add user")
    @allure.title("Empty name raises ValueError")
    def test_add_user_empty_name(self):
        self.user.name = ""
        with self.assertRaises(ValueError):
            self.manager.add_user(self.user)

    @allure.story("Add user")
    @allure.title("Short name raises ValueError")
    def test_add_user_short_name(self):
        self.user.name = "A"
        with self.assertRaises(ValueError):
            self.manager.add_user(self.user)

    @allure.story("Add user")
    @allure.title("Invalid name type raises TypeError")
    def test_add_user_invalid_name_type(self):
        self.user.name = 5
        with self.assertRaises(TypeError):
            self.manager.add_user(self.user)


    @allure.story("Add user")
    @allure.title("Negative age raises ValueError")
    def test_add_user_negative_age(self):
        self.user.age = -20
        with self.assertRaises(ValueError):
            self.manager.add_user(self.user)


    @allure.story("Add user")
    @allure.title("Age greater than 120 raises ValueError")
    def test_add_user_large_age(self):
        self.user.age = 111
        with self.assertRaises(ValueError):
            self.manager.add_user(self.user)

    @allure.story("Add user")
    @allure.title("Invalid age type raises TypeError")
    def test_add_user_invalid_age_type(self):
        self.user.age = "25"
        with self.assertRaises(TypeError):
            self.manager.add_user(self.user)

    @allure.story("Add user")
    @allure.title("Invalid email raises ValueError")
    def test_add_user_invalid_email(self):
        pass

    @allure.story("Add user")
    @allure.title("Invalid email type raises TypeError")
    def test_add_user_invalid_email(self):
        self.user.email = "alicemail.ru"
        with self.assertRaises(ValueError):
            self.manager.add_user(self.user)

    @allure.story("Get user")
    @allure.title("Get existing user")
    def test_add_user_invalid_email_type(self):
        self.user.email = test
        with self.assertRaises(TypeError):
            self.manager.add_user(self.user)

    @allure.story("Get user")
    @allure.title("Get missing user")
    def test_get_existing_user(self):
        self.manager.add_user(self.user)
        self.assertEqual(self.manager.get_user(1), self.user)

    @allure.story("Remove user")
    @allure.title("Remove existing user")
    def test_get_missing_user(self):
        self.assertIsNone(self.manager.get_user(222))

    @allure.story("Remove user")
    @allure.title("Remove missing user")
    def test_remove_user(self):
        self.manager.add_user(self.user)
        self.manager.remove_user(self.user.id)
        self.assertEqual(self.manager.count_users(), 0)

    @allure.story("Get all users")
    @allure.title("Get users from empty manager")
    def test_get_all_users_empty(self):
        self.assertEqual(self.manager.get_all_users(), [])

    @allure.story("Get all users")
    @allure.title("Get users list")
    def test_get_all_users(self):
        self.manager.add_user(self.user)
        self.assertEqual(self.manager.get_all_users(), [self.user])

    @allure.story("Count users")
    @allure.title("Count users in empty manager")
    def test_count_users_empty(self):
        self.assertEqual(self.manager.count_users(), 0)

    @allure.story("Count users")
    @allure.title("Count users")
    def test_count_users(self):
        self.manager.add_user(self.user)
        self.assertEqual(self.manager.count_users(), 1)