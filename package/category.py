import conf
import note

class Category(conf.Base):
    __tablename__ = 'categories'

    id = conf.Column(conf.Integer, primary_key=True)
    name = conf.Column(conf.String(10), nullable=False, unique=True)

    @classmethod
    def search_by_name(cls, name):
        return conf.session.query(Category).filter(Category.name == name)

    @classmethod
    def find_by_name(cls, name):
        return conf.session.query(Category).filter(Category.name == name).one()

    def save(self):
        conf.save_to_db(self)

    def notes(self):
        return conf.session.query(note.Note).filter(note.Note.category_id == self.id)
