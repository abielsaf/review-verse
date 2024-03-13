"""empty message

Revision ID: 2081415f6aa8
Revises: 
Create Date: 2024-03-12 15:57:58.202056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2081415f6aa8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('author', sa.String(length=50), nullable=True),
    sa.Column('published_year', sa.String(length=50), nullable=True),
    sa.Column('pages', sa.Integer(), nullable=True),
    sa.Column('thumbnail', sa.String(length=200), nullable=True),
    sa.Column('small_thumbnail', sa.String(length=200), nullable=True),
    sa.Column('google_id', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('book_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('hash', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('visibility', sa.String(length=10), server_default='public', nullable=False),
    sa.CheckConstraint("visibility IN ('public', 'private')", name='visibility_check'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('review',
    sa.Column('review_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.book_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('review_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.drop_table('user')
    op.drop_table('book')
    # ### end Alembic commands ###
