"""empty message

Revision ID: 37df76126f26
Revises: 762402052503
Create Date: 2021-02-23 23:18:10.207095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37df76126f26'
down_revision = '762402052503'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo_lis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.Column('label', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo_lis')
    # ### end Alembic commands ###
