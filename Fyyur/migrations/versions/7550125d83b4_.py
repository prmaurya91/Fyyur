"""empty message

Revision ID: 7550125d83b4
Revises: 952fe3f46484
Create Date: 2020-05-08 15:49:48.487037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7550125d83b4'
down_revision = '952fe3f46484'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=250), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'seeking_description')
    # ### end Alembic commands ###
