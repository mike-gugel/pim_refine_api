"""ext datasources models

Revision ID: b9f7e4b0d1c8
Revises: 26ffd3d6bcd5
Create Date: 2022-07-08 12:54:10.801828

"""
from alembic import op
import sqlalchemy as sa
import ormar
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b9f7e4b0d1c8'
down_revision = '26ffd3d6bcd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crawlab_info',
    sa.Column('ean', sa.String(length=13), nullable=False),
    sa.Column('info', sa.JSON(), nullable=False),
    sa.Column('task_id', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
    sa.PrimaryKeyConstraint('ean')
    )
    op.create_index(op.f('ix_crawlab_info_ean'), 'crawlab_info', ['ean'], unique=True)
    op.create_table('icecat_info',
    sa.Column('ean', sa.String(length=13), nullable=False),
    sa.Column('info', sa.JSON(), nullable=False),
    sa.Column('requested_by', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
    sa.Column('requested_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('ean')
    )
    op.create_index(op.f('ix_icecat_info_ean'), 'icecat_info', ['ean'], unique=True)
    op.create_table('paw_info',
    sa.Column('variant_id', sa.String(length=15), nullable=False),
    sa.Column('info', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('variant_id')
    )
    op.create_index(op.f('ix_paw_info_variant_id'), 'paw_info', ['variant_id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apscheduler_jobs',
    sa.Column('id', sa.VARCHAR(length=191), autoincrement=False, nullable=False),
    sa.Column('next_run_time', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('job_state', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='apscheduler_jobs_pkey')
    )
    op.create_index('ix_apscheduler_jobs_next_run_time', 'apscheduler_jobs', ['next_run_time'], unique=False)
    op.drop_index(op.f('ix_paw_info_variant_id'), table_name='paw_info')
    op.drop_table('paw_info')
    op.drop_index(op.f('ix_icecat_info_ean'), table_name='icecat_info')
    op.drop_table('icecat_info')
    op.drop_index(op.f('ix_crawlab_info_ean'), table_name='crawlab_info')
    op.drop_table('crawlab_info')
    op.drop_table('PIM_query29')
    op.drop_table('PIM_query20_5')
    # ### end Alembic commands ###
