# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore


__protobuf__ = proto.module(
    package="google.bigtable.v2",
    manifest={
        "FeatureFlags",
    },
)


class FeatureFlags(proto.Message):
    r"""Feature flags supported or enabled by a client. This is intended to
    be sent as part of request metadata to assure the server that
    certain behaviors are safe to enable. This proto is meant to be
    serialized and websafe-base64 encoded under the
    ``bigtable-features`` metadata key. The value will remain constant
    for the lifetime of a client and due to HTTP2's HPACK compression,
    the request overhead will be tiny. This is an internal
    implementation detail and should not be used by end users directly.

    Attributes:
        reverse_scans (bool):
            Notify the server that the client supports
            reverse scans. The server will reject
            ReadRowsRequests with the reverse bit set when
            this is absent.
        mutate_rows_rate_limit (bool):
            Notify the server that the client enables
            batch write flow control by requesting
            RateLimitInfo from MutateRowsResponse. Due to
            technical reasons, this disables partial
            retries.
        mutate_rows_rate_limit2 (bool):
            Notify the server that the client enables
            batch write flow control by requesting
            RateLimitInfo from MutateRowsResponse. With
            partial retries enabled.
        last_scanned_row_responses (bool):
            Notify the server that the client supports the
            last_scanned_row field in ReadRowsResponse for long-running
            scans.
    """

    reverse_scans: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    mutate_rows_rate_limit: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    mutate_rows_rate_limit2: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    last_scanned_row_responses: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
