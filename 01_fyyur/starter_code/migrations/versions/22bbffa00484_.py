"""empty message

Revision ID: 22bbffa00484
Revises: bc6c102d525e
Create Date: 2020-02-17 14:22:00.401974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22bbffa00484'
down_revision = 'bc6c102d525e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('genres', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    op.add_column('Artist', sa.Column('availability', sa.ARRAY(sa.String()), nullable=True)),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Artist')
    # ### end Alembic commands ###
