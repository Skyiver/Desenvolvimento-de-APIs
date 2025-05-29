from models import db
from datetime import date, datetime

class Aluno(db.Model):
    __tablename__ = 'alunos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'))
    data_nascimento = db.Column(db.String(10))
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    media_final = db.Column(db.Float)

    def _calcula_idade(self):
        if not self.data_nascimento:
            return None
        try:
            # data_nascimento no formato 'YYYY-MM-DD'
            nasc = datetime.strptime(self.data_nascimento, "%Y-%m-%d").date()
            hoje = date.today()
            anos = hoje.year - nasc.year - ((hoje.month, hoje.day) < (nasc.month, nasc.day))
            return anos
        except ValueError:
            return None

    def _calcula_media(self):
        if self.nota_primeiro_semestre is None or self.nota_segundo_semestre is None:
            return None
        return (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self._calcula_idade(),
            'turma_id': self.turma_id,
            'data_nascimento': self.data_nascimento,
            'nota_primeiro_semestre': self.nota_primeiro_semestre,
            'nota_segundo_semestre': self.nota_segundo_semestre,
            'media_final': self._calcula_media()
        }