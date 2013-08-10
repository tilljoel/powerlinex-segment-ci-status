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
        for line in readlines(["sh", "/Users/joel/bin/ci-status-wrapper.sh"], segment_info['getcwd']()):
            if line == 'success':
                return [{
                    'contents': 'success',
                    'highlight_group': ['ci-status', 'virtualenv']
                }]
            else:
                return [{
                    'contents': 'failure',
                    'highlight_group': ['ci-status', 'virtualenv']
                }]
    except OSError as e:
        if e.errno == 2:
            pass
        else:
            raise
