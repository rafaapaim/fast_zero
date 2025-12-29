from sqlalchemy import select

from src.models import User


def test_create_user(session):
    user = User(username='rafael', email='email@email.com', password='senha')

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'email@email.com')
    )

    assert result.username == 'rafael'
