"""empty message

Revision ID: 4d8ffdde0a4a
Revises: 1c97414a4e06
Create Date: 2019-11-27 22:59:53.259714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d8ffdde0a4a'
down_revision = '1c97414a4e06'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tournaments', sa.Column('city', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tournaments', 'city')
    # ### end Alembic commands ###
