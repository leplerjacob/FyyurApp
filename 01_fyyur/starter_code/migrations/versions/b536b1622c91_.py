"""empty message

Revision ID: b536b1622c91
Revises: 64ff541b248d
Create Date: 2020-02-28 11:08:33.184109

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b536b1622c91'
down_revision = '64ff541b248d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Availability',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('dates', sa.String(), nullable=True),
    sa.Column('times', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('Artist', 'availability')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('availability', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.drop_table('Availability')
    # ### end Alembic commands ###
