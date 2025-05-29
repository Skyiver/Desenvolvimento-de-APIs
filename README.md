# API Escolar (School System)

Este repositório contém a API de Gerenciamento Escolar, um microsserviço responsável por gerenciar Professores, Alunos e Turmas. Desenvolvido com Flask, SQLAlchemy e PostgreSQL, faz parte de uma arquitetura de microsserviços integrada com as APIs de Atividades e Reserva de Salas.

---

## 🧩 Arquitetura

* **escola\_service**: microsserviço que expõe CRUD para entidades:

  * **Professores**
  * **Alunos**
  * **Turmas**
* **atividade\_service**: consome esta API para validação de professores (repositório: [https://github.com/Skyiver/devapiatividade.git](https://github.com/Skyiver/devapiatividade.git))
* **reserva\_salas\_service**: consome esta API para validação de turmas (repositório: [https://github.com/Skyiver/devapisalas.git](https://github.com/Skyiver/devapisalas.git))

A comunicação entre serviços se dá via HTTP REST. Por exemplo, `atividade_service` chama:

```
GET http://<host>:5002/api/professores/<id>
```

para verificar se o professor existe.

---

## 🚀 Tecnologias Utilizadas

* Python 3.13
* Flask 3.1.0
* Flask-SQLAlchemy 3.1.1
* PostgreSQL 15 (via Docker)
* Flask-RESTX (Swagger/OpenAPI)
* Pytest + requests para testes automatizados
* Docker & Docker Compose

---

## ▶️ Como Executar a API

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/Skyiver/Desenvolvimento-de-APIs.git
   cd Desenvolvimento-de-APIs
   ```

2. **Suba os serviços**:

   ```bash
   docker-compose up --build
   ```

3. **Acesse**:

   * Base URL: `http://localhost:5002/api`
   * Swagger UI: `http://localhost:5002/docs`

---

## 📡 Endpoints Principais

### Professores

* `GET  /api/professores`
* `POST /api/professores`
* `GET  /api/professores/<id>`
* `PUT  /api/professores/<id>`
* `DELETE /api/professores/<id>`

### Alunos

* `GET  /api/alunos`
* `POST /api/alunos`
* `GET  /api/alunos/<id>`
* `PUT  /api/alunos/<id>`
* `DELETE /api/alunos/<id>`

### Turmas

* `GET  /api/turmas`
* `POST /api/turmas`
* `GET  /api/turmas/<id>`
* `PUT  /api/turmas/<id>`
* `DELETE /api/turmas/<id>`

---

## 🛠️ Exemplos de Uso com cURL

```bash
# Criar Aluno
curl -X POST http://localhost:5002/api/alunos \
  -H "Content-Type: application/json" \
  -d '{"nome":"Joao","id":11,"turma_id":3,"data_nascimento":"2004-03-22"}'

# Listar Professores
curl http://localhost:5002/api/professores

# Atualizar Turma
curl -X PUT http://localhost:5002/api/turmas/5 \
  -H "Content-Type: application/json" \
  -d '{"nome":"Turma X - Revisada"}'
```

---

## 📦 Estrutura do Projeto

```
Desenvolvimento-de-APIs/
│
├── app.py
├── config.py
├── models/
│   ├── aluno.py
│   ├── professor.py
│   └── turma.py
├── routes/
│   ├── alunos.py
│   ├── professores.py
│   ├── turmas.py
│   └── reset_routes.py
├── services/
│   ├── aluno_service.py
│   ├── professor_service.py
│   ├── turma_service.py
│   └── auth_service.py      # Autenticação JWT
├── utils/
│   └── reset_routes.py      # Rota para testes de reset
├── tests/
│   ├── test_api.py
│   └── test_integration_postgres.py  # Teste de integração com Postgres
├── docker-compose.yml       # Inclui web e db (Postgres)
├── requirements.txt
└── README.md
```

---

## 🧪 Testes Automatizados

* **test\_api.py**: testes unitários de CRUD com reset in-memory
* **test\_integration\_postgres.py**: testes de integração real contra Postgres

Para executar:

```bash
pytest -v
```

---

## 🛠️ Futuras Melhorias

* Autenticação JWT para proteger endpoints.
* Logs estruturados e monitoramento.
* Versionamento da API.
* Healthcheck integrado e retry/fallback para dependências.

---

## 🧑‍💻 Autores

* Akira Ogassavara (Curso de SI – Impacta)
* Amanda Costa (Curso de SI – Impacta)
