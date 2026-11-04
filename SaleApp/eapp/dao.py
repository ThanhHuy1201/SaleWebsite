from eapp.models import Category


def load_category():
    return Category.query.all()