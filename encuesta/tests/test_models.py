from django.contrib.auth.models import User
from django.test import TestCase

from encuesta.models import Choice, Images


class Setup_Choice(TestCase):
    def setUpTestData(clf):
        clf.choice = Choice.objects.create(
            usuario="user", imagen="Image_name", voto="A"
        )


class Choice_Test(TestCase):
    def test_Choice_valid(self):
        # Crea un voto válido (con una imágen vacía)
        user = User()
        user.save()
        imagen_test = Images()
        choice = Choice(usuario=user, imagen=imagen_test, voto="A")
        self.assertEqual(choice.voto, "A")
