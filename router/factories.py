from .models import Person
import factory

class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    name = factory.Faker('name')
    last_name = factory.Faker('last_name')
    age = factory.Faker('random_int', min=18, max=65)

