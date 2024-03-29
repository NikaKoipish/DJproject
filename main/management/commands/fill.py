from django.core.management import BaseCommand
from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **options):

        students_list = [
            {"last_name": "Сидорова", "first_name": "Арина"},
            {"last_name": "Иванова", "first_name": "Анастасия"},
            {"last_name": "Петрова", "first_name": "Ольга"},
            {"last_name": "Александрова", "first_name": "Инна"}
        ]

        students_for_create = []
        for student_item in students_list:
            students_for_create.append(Student(**student_item))

        Student.objects.bulk_create(students_for_create)