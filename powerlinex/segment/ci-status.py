from __future__ import absolute_import
from subprocess import Popen, PIPE
from powerline.theme import requires_segment_info


def readlines(cmd, cwd):
    p = Popen(cmd, shell=False, stdout=PIPE, stderr=PIPE, cwd=cwd)
    p.stderr.close()
    with p.stdout:
        for line in p.stdout:
            yield line[:-1].decode('utf-8')


@requires_segment_info
def version(pl, segment_info):
    try:
        # ci-status --reporter=minimal
        for line in readlines(["ci-status", "--reporter=minimal"], segment_info['getcwd']()):
            # Now to process line
            return [{
                'contents': 'success',
                'highlight_group': ['ci-status', 'virtualenv']
            }]
    except OSError as e:
        if e.errno == 2:
            pass
        else:
            raise
