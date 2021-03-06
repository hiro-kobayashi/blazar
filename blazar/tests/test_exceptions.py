# Copyright (c) 2013 Bull.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import six

from blazar import exceptions
from blazar import tests


class BlazarExceptionTestCase(tests.TestCase):
    def test_default_error_msg(self):
        class FakeBlazarException(exceptions.BlazarException):
            msg_fmt = "default message"

        exc = FakeBlazarException()
        self.assertEqual(six.text_type(exc), 'default message')

    def test_error_msg(self):
        self.assertEqual(six.text_type(exceptions.BlazarException('test')),
                         'test')

    def test_default_error_msg_with_kwargs(self):
        class FakeBlazarException(exceptions.BlazarException):
            msg_fmt = "default message: %(code)s"

        exc = FakeBlazarException(code=500)
        self.assertEqual(six.text_type(exc), 'default message: 500')
        self.assertEqual(str(exc), 'default message: 500')

    def test_error_msg_exception_with_kwargs(self):
        class FakeBlazarException(exceptions.BlazarException):
            msg_fmt = "default message: %(mispelled_code)s"

        exc = FakeBlazarException(code=500, mispelled_code='blah')
        self.assertEqual(six.text_type(exc), 'default message: blah')
        self.assertEqual(str(exc), 'default message: blah')

    def test_default_error_code(self):
        class FakeBlazarException(exceptions.BlazarException):
            code = 404

        exc = FakeBlazarException()
        self.assertEqual(exc.kwargs['code'], 404)

    def test_error_code_from_kwarg(self):
        class FakeBlazarException(exceptions.BlazarException):
            code = 500

        exc = FakeBlazarException(code=404)
        self.assertEqual(exc.kwargs['code'], 404)

    def test_policynotauthorized_exception(self):
        exc = exceptions.PolicyNotAuthorized(action='foo')
        self.assertEqual(six.text_type(exc),
                         "Policy doesn't allow foo to be performed")
        self.assertEqual(exc.kwargs['code'], 403)
