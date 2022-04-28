"""empty message

Revision ID: 15faa409cdee
Revises: 
Create Date: 2022-04-27 14:48:02.567052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15faa409cdee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('presets', sa.Column('preset_number', sa.Integer(), nullable=True))
    op.alter_column('presets', 'octave',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)
    op.alter_column('presets', 'attack',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)
    op.alter_column('presets', 'decay',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)
    op.alter_column('presets', 'release',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)
    op.alter_column('presets', 'waveforms',
               existing_type=sa.REAL(),
               type_=sa.Float(precision=5),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('presets', 'waveforms',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)
    op.alter_column('presets', 'release',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)
    op.alter_column('presets', 'decay',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)
    op.alter_column('presets', 'attack',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)
    op.alter_column('presets', 'octave',
               existing_type=sa.Float(precision=5),
               type_=sa.REAL(),
               existing_nullable=False)
    op.drop_column('presets', 'preset_number')
    # ### end Alembic commands ###