import conf
import category

class Note(conf.Base):
    __tablename__ = 'notes'

    id = conf.Column(conf.Integer, primary_key=True)
    text = conf.Column(conf.Text, nullable=False)
    category_id = conf.Column(
                        conf.Integer,
                        conf.ForeignKey('categories.id'),
                        nullable=False)
    category = conf.relationship(category.Category)

    def save(self):
        conf.save_to_db(self)
